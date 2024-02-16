import random

class SlotMachine:
    def __init__(self, n, p, value):
        self.id = n
        self.p = p
        self.value = value
    
    def pull_bandit(self) -> int:
        result = random.random()

        if(result <= self.p):
            return self.value
        else:
            return 0

class Agent:
    def __init__(self, bandits_list, epsilon):
        self.epsilon = epsilon
        self.bandits_list = bandits_list
        self.best_bandit = None
        self.best_reward = 0 #a que tem o maior valor/chance
        self.bandits_data = []
        for bandit in bandits_list:
            self.bandits_data.append({"id":bandit.id, "rewards":[], "mean":0})

    def pull_bandit(self, bandit : SlotMachine):
        for bandit_element in self.bandits_data:
            if(bandit_element['id'] == bandit.id):
                reward = bandit.pull_bandit()
                bandit_element['rewards'].append(reward)
                
                bandit_element['mean'] = sum(bandit_element['rewards'])/len(bandit_element['rewards'])
                if(bandit_element['mean'] > self.best_reward):
                    self.best_bandit = bandit
                    self.best_reward = bandit_element['mean']
                if(self.best_bandit != None):
                    if(bandit_element['id'] == self.best_bandit.id):
                        #se a recompensa não aumentou e eu tô atualizando o "melhor" pode significar que ela baixou para ele
                        #Preciso checar agora qual o melhor de todos
                        best_bandit = max(self.bandits_data, key=lambda x: x['mean'])
                        self.best_reward = best_bandit['mean']
                        self.best_bandit = next(bandit for bandit in self.bandits_list if bandit.id == best_bandit['id'])

                break
        return reward

    def explore(self):
        bandit = random.choice(self.bandits_list)
        self.pull_bandit(bandit)

    def exploit(self):
        if(self.best_bandit != None):
            self.pull_bandit(self.best_bandit)

    def episilon_greedy(self):
        if(random.random() > self.epsilon and self.best_bandit): #Enquanto ele não tiver um melhor ele não exploita
            self.exploit()
        else:
            self.explore()



slot_machines_data = [
    {"n": 0, "p": 0.05, "value": 100},
    {"n": 1, "p": 0.10, "value": 50},
    {"n": 2, "p": 0.15, "value": 30},
    {"n": 3, "p": 0.03, "value": 500},
    {"n": 4, "p": 0.08, "value": 80},
    {"n": 5, "p": 0.12, "value": 40},
    {"n": 6, "p": 0.07, "value": 70},
    {"n": 7, "p": 0.06, "value": 60},
    {"n": 8, "p": 0.09, "value": 90},
    {"n": 9, "p": 0.11, "value": 110}
]

slot_machines = []
for sm in slot_machines_data:
    slot_machines.append(SlotMachine(sm['n'], sm['p'], sm['value']))

agent = Agent(slot_machines, 0.3)

for i in range(8000):
    agent.episilon_greedy()

print(agent.best_bandit.id)


for data in agent.bandits_data:
    recompensa_esperada = 0
    if(len(data['rewards']) != 0):
        recompensa_esperada = sum(data['rewards'])/len(data['rewards'])
    print(f"bandit de id: {data['id']} tem recompensa esperada: {recompensa_esperada}")