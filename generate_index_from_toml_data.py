import tomllib


with open('char_to_blueprint_shorts.toml', 'rb') as fp:
    char_to_blueprint_shorts = tomllib.load(fp)


print('# Mandarin Blueprint character Youtube shorts index')
print()
for char, shorts in char_to_blueprint_shorts.items():
    print(f'- {char}')
    for short in shorts:
        print(f'    - [{short["title"]}]({short["url"]})')
