# Minimal Tool class for demonstration
class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, input_text):
        # Example tool logic
        return f"Tool '{self.name}' used with input: {input_text}"
