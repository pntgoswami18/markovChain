import random
import string


class MarkovModel:

    def __init__(self):
        self.model = None

    def learn(self, tokens, n=2):
        model = {}
        tokens = tokens.split()
        length = len(tokens)

        for i in range(0, length-n):
            gram = tuple(tokens[i:i+n])
            token = tokens[i+n]

            if gram in model:
                model[gram].append(token)
            else:
                model[gram] = [token]

        final_gram = tuple(tokens[len(tokens) - n:])
        if final_gram in model:
            model[final_gram].append("#END#")
        else:
            model[final_gram] = ["#END#"]
        self.model = model
        print(model)
        return model

    def generate(self, n=2, seed=None, max_tokens=100):
        if seed is None:
            seed = random.choice(list(self.model.keys()))

        output = list(seed)
        output[0] = output[0].capitalize()
        current = seed

        for i in range(n, max_tokens):
            # get next possible set of words from the seed word
            # print(current)
            if current in self.model:
                possible_transitions = self.model[current]
                choice = random.choice(possible_transitions)
                if choice is "#END#":
                    break

                if choice == '.':
                    output[-1] = output[-1] + choice
                else:
                    output.append(choice)
                current = tuple(output[-n:])
            else:
                # should return ending punctuation of some sort
                if current[1] not in string.punctuation:
                    if current[1] == '#END#':
                        break
                    else:
                        output.append('.')

        return output


mm = MarkovModel()
mm.learn("It's worth noting that this wasn't obvious to at least 133 people who took time to up vote (myself included) who didn't understand this.")
print("~~~~~~\nnow generating\n~~~~~~~")
generatedIterable = mm.generate()
s = ' '
print(s.join(generatedIterable))
