import random
import time

# levels
levels = {
    "level_1": {
        "range": (1, 10),
        "operator": "+",
        "shortcode": "1"
    },
    "level_2": {
        "range": (1, 10),
        "operator": "+",
        "shortcode": "1"
    }
}


def level_select():
  print("Select a level:")
  for details in levels.values():
    print(f"- {details['shortcode']}")
  selected_shortcode = input("Enter the level name: ")
  selected_level = next((level for level, details in levels.items()
                         if details['shortcode'] == selected_shortcode), None)
  if selected_level is None:
    print("Invalid level selected.")
    return level_select()
  return selected_level


def gen_prob_lvl_1(num_problems):
  problems = []
  for _ in range(num_problems):
    # generate two random numbers between 1 and 9
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    # ensure the sume does not exceed 10
    while num1 + num2 > 10:
      num1 = random.randint(1, 9)
      num2 = random.randint(1, 9)

    # calulate the answer
    answer = num1 + num2

    # append the problem to the list
    problems.append({
        'num1': num1,
        'num2': num2,
        'operator': '+',
        'answer': answer
    })
  return problems


def run_generator(selected_level, num_problems):
  problems = []
  if selected_level == "level_1":
    problems = gen_prob_lvl_1(num_problems)
  elif selected_level == "level_2":
    problems = gen_prob_lvl_2(num_problems)
  else:
    print("Invalid level selected: ", selected_level)
  return problems


def run_quiz(problems):
  correct = 0
  incorrect = 0
  start_time = time.time()
  for problem in problems:
    if time.time() - start_time >= 20:
      print("Time's up!")
      break
    answer = int(
        input(f"{problem['num1']} {problem['operator']} {problem['num2']} = "))
    problem['input'] = answer
    if answer == problem['answer']:
      # print("Correct!")
      correct += 1
    else:
      incorrect += 1

  print(f"You got {correct} out of {correct + incorrect} correct.")
  return correct, incorrect, problems


def main():
  level = level_select()
  print(f"You selected {level}.")

  num_problems = 20

  problems = run_generator(level, num_problems)

  correct, incorrect, problems = run_quiz(problems)
  for problem in problems:
    print(problem)


if __name__ == '__main__':
  main()
