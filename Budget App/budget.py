class Category:
  # Instance variables, category name and a ledger
  def __init__(self, type_category):
    self.type = type_category
    self.ledger = []

  def get_balance(self):
    bal = 0
    for entry in self.ledger:
      bal += entry["amount"]
    return bal

  # Check funds must be declared before withdraw and transfer
  def check_funds(self, amount):
    return amount <= self.get_balance()

  def deposit(self, amount: float, description: str = ""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount: float, description: str = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def transfer(self, amount: float, other):
    if self.check_funds(amount):
      self.ledger.append({
          "amount": -amount,
          "description": f"Transfer to {other.type}"
      })
      other.ledger.append({
          "amount": amount,
          "description": f"Transfer from {self.type}"
      })
      return True
    return False

  # Change __str__ so we control what is displayed when we print a category object
  def __str__(self):
    printed = ""
    total = 0.00

    # Category name titles, centred with asterik surrounding
    printed += self.type.center(30, "*") + "\n"

    # FOR loop to print every ledger entry (transaction), formatted.
    for i in self.ledger:
      total += i["amount"]
      printed += i["description"].ljust(23, " ")[:23]
      printed += ("{:.2f}".format(i["amount"])).rjust(7, " ") + "\n"
    printed += "Total: " + "{:.2f}".format(total)
    return printed


def create_spend_chart(categories: list):
  # Chart title
  out = "Percentage spent by category\n"

  # Initialise some variables to calculate percentage spend of each category
  grand_total = 0
  expenses = []
  types = []
  for i in categories:
    total = sum(-j["amount"] for j in i.ledger if j["amount"] < 0)
    grand_total += total
    expenses.append(total)
    types.append(i.type)

  # Calculate percentages with a comprehension !!!
  percentages = [x / grand_total * 100 for x in expenses]

  # FOR loop to print percentages
  for k in range(100, -1, -10):
    out += str(k).rjust(3, " ") + "|"
    for p in percentages:
      if p >= k:
        out += " o "
      else:
        out += "   "
    out += " \n"

  # Add the horizontal dashed line
  out += "    " + "-" * 3 * len(types) + "-\n"

  # Here we find the longest category name
  # This will determine size of a FOR loop later
  longest_name_length = len(types[0])
  for t in types:
    if len(t) > longest_name_length:
      longest_name_length = len(t)

  # Now we print all names letter by letter, until some are just space marks
  for letter_index in range(longest_name_length):
    out += "    "
    for t in types:
      if letter_index < len(t):
        out += f" {t[letter_index]} "
      else:
        out += "   "
    out += " "
    if letter_index != longest_name_length - 1:
      out += "\n"
  return out