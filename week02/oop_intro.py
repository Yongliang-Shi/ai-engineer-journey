# oop_intro.py
# Week 2 — OOP practice
#
# A small Task/Bug tracker demonstrating:
#   - instance vs. class attributes
#   - constructor validation, raising a custom exception on bad input
#   - @classmethod as an alternative constructor with input validation
#   - inheritance
#   - operator overloading
#   - string representations

class InvalidPriorityError(Exception):
    pass

class Task:
    VALID_PRIORITY_LEVELS = ['Urgent', 'High', 'Medium', 'Low']

    def __init__(self, title, priority):
        self.title = title

        if priority not in self.VALID_PRIORITY_LEVELS:
            raise InvalidPriorityError("Priority isn't valid")

        self.priority = priority

    @classmethod
    def from_line(cls, csv_line):
        parts = csv_line.split("-")
        if len(parts) != 2:
            raise ValueError(f"Expected 'title-priority', got: {csv_line}")
        title, priority = parts[0].strip(), parts[1].strip()
        return cls(title, priority)
    
    def close(self):
        print("Close {} priority task {}".format(self.priority, self.title))

    def __repr__(self):
        str_name = type(self).__name__
        str_repr = f"{str_name}({self.title}, {self.priority})"
        return str_repr

    def __str__(self):
        str_name = type(self).__name__
        str_readable = f"""{str_name} title: {self.title}\n{str_name} priority: {self.priority}"""
        return str_readable

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.title.lower() == other.title.lower()) and (self.priority.lower() == other.priority.lower())

class Bug(Task):
    def __init__(self, title, priority, severity):
        super().__init__(title, priority)
        self.severity = severity

    def __str__(self):
        str_super = super().__str__()
        str_name = type(self).__name__
        str_readable = str_super + f"""\n{str_name} severity: {self.severity}"""
        return str_readable

if __name__ == "__main__":
    t = Task("Fix login bug", "High")
    print(repr(t))
    print(t)
    t.close()
 
    b = Bug("Crash on save", "Urgent", severity="Critical")
    print(repr(b))
    print(b)
 
    t2 = Task.from_line("Update docs - Low")
    print(t2)
 
    print(Task("Same Task", "High") == Task("same task", "High"))