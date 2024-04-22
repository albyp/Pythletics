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


def main():
  level = level_select()
  print(f"You selected {level}.")

  num_problems = 20

  problems = gen_prob_lvl_1(num_problems)
  for problem in problems:
    print(problem)


if __name__ == '__main__':
  main()
