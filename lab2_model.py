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

agent = StatefulAgent()
percepts = [(29, True), (29, True), (26, True), (20, True),
            (19, True), (29, False), (29, False), (24, True)]

for p in percepts:
    prev = agent.last
    target, send = agent.act(*p)
    if send:
        result = "send command"
    else:
        result = "no command"
    print("previous:", prev, "| percept:", p, "| target:", target, "|", result)
