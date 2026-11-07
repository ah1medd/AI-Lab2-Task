class StatefulAgent:
    def __init__(self):
        self.last = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"
        send = target != self.last
        self.last = target
        return target, send

# noisy readings around 26 degrees
readings = [25.9, 26.1, 25.8, 26.2, 26.0, 26.3, 25.9]
agent = StatefulAgent()
commands = 0
for t in readings:
    prev = agent.last
    target, send = agent.act(t, True)
    if send:
        commands += 1
    print("previous:", prev, "| temp:", t, "| target:", target, "| send:", send)
print("readings:", len(readings), "commands sent:", commands)

# same 8 percepts for both agents
percepts = [(29, True), (29, True), (26, True), (20, True),
            (19, True), (29, False), (29, False), (24, True)]
a = StatefulAgent()
stateful_commands = 0
for p in percepts:
    if a.act(*p)[1]:
        stateful_commands += 1
print("reflex agent sends", len(percepts), "commands, stateful agent sends", stateful_commands)
