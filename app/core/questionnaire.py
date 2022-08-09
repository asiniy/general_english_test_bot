from dataclasses import dataclass

@dataclass
class Question:
  title: str
  options: list[str]

questions = [
  Question("Can I park here?", ["Only for half an hour", "Sorry, I did that", "It's the same place"]),
  Question("What colour will you paint the children's bedroom?", ["We can't decide.", "I hope it was right.", "It wasn't very difficult."]),
  Question("I can't understand this email.", ["Would you like some help?", "Don't you know?", "I suppose you can."]),
  Question("I'd like two tickets for tomorrow night.", ["I'll just check for you.", "How much did you pay?", "Afternoon and evening."]),
  Question("Shall we go to the gym now?", ["I'm too tired.", "It's very good.", "Not at all."]),
]
