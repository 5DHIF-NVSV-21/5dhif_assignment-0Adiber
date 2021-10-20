import json
from os import system, name
from action import options, Action

def clear():
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
  # read json
  j = json.load(open('motivation.json'))
  actions = Action(**j)

  # main loop for choices
  while True:
    clear()
    print('''\nWhat do you want me to do?
        [1] Motivate me
        [2] Take me back to reality
        [3] Show me something cute
        [9] Exit

    ''')

    while True:
      try:
        choice: int = int(input("Choice: "))
        
        if choice == options["EXIT"]:
          exit()
        else:
          res = actions.getChoice(choice)
          if res != None:
            res.render()
            break
          else:
            print('Please pick one of the above')
      except ValueError:
        print('Please enter a number')
        continue
      except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()