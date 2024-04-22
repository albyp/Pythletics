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
  for details in levels.valuess():
    print(f"- {details['shotcode']}")
  selected_shortcode = input("Enter the level name: ")
  selected_level = next((level for level, details in levels.items()
                        if details['shortcode'] == selected_shortcode), None)
  if selected_level is None:
    print("Invalide level selected.")
    return level_select()
  return selected_level

def main():
  level = level_select()
  print(f"You selected {level}.")


if __name__ == '__main__':
  main()
