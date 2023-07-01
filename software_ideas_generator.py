import random

# Lists of words for the software ideas generator
keywords = ['Application', 'System', 'Platform', 'Tool', 'Service', 'Interface']
actions = ['management', 'monitoring', 'optimization', 'analysis', 'automation']
targets = ['projects', 'tasks', 'processes', 'data', 'reports']
extensions = ['for businesses', 'for learning', 'for developers', 'for commerce', 'for e-commerce']

# Generate a software idea
def generate_idea():
    idea = random.choice(keywords) + ' ' + random.choice(actions) + ' ' + random.choice(targets)
    extension = random.choice(extensions)
    if random.randint(0, 1):
        idea += ' ' + extension
    return idea

# Main program loop
def main():
    print('--- Software Ideas Generator ---\n')
    print('Generated software idea:')
    idea = generate_idea()
    print(idea)

if __name__ == '__main__':
    main()
