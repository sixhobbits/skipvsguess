import random
import string

class Exam:
    questions = None
    answers = None
    
    def __init__(self, num_questions, num_answers):
        self.questions = range(num_questions)
        self.answers = []
        
        possible_answers = string.ascii_lowercase[:num_answers]
        
        for question in range(num_questions):
            answer = random.choice(possible_answers)
            self.answers.append(answer)
        
        
    # answer right
    # - get one point
    # answer wrong
    # - lose half a point
    # - if answer >= 4:
    # - lose 1 point PER ANSWER (including first three)
    # don't answer
    # - nothing
    
    def score(self, guesses):
        correct = 0
        incorrect = 0 
        for i, guess in enumerate(guesses):
            if not guess:
                continue  # didn't answer, no effect on score
            elif guess == self.answers[i]:
                correct += 1
            else:
                # wrong answer
                incorrect += 1
        if incorrect >= 4:
            lost_points = incorrect
        else:
            lost_points = incorrect / 2
        
        return correct - lost_points


# If I know between 0 and four answers, how many should i guess?

win = 0
attempts = 1000000 # try a bunch of times because stats

e = Exam(10, 3) # our exam has 10 questions and three possible answers per question

oracles = 5  # oracle is number of questions to magically get right - if we know more than 5 then we win by default
skips = 10  # skips is to replace some random guesses with None - we can skip up to 10 questions

for oracle in range(oracles):
    print("oracle", oracle)
    for skip in range(skips):
        win = 0
        print("    ...skip", skip)
        if oracle + (10-skip) > 10:
            continue
        for attempt in range(attempts):
            guesses = [random.choice("abc") for x in range(10)]
            for n in range(skip):
                guesses[n] = None
            for o in range(1,oracle+1):  # we get a free answer for each of these
                guesses[-o] = e.answers[-o]
            score = e.score(guesses)
            if score >= 5:
                win += 1
        print("    ", round(win/attempts*100, 1))
