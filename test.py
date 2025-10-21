data={'Alex': {'game': 'Minecraft', 'score': 54}, 'Ben': {'game': 'Fortnite', 'score': 88}, 'Chloe': {'game': 'FIFA', 'score': 42}, 'Dylan': {'game': 'Minecraft', 'score': 71}, 'Ella': {'game': 'FIFA', 'score': 1000}}

def write_to_file(filename, dict_to_write):
    filewrite = open(filename, "w")
    for i in dict_to_write:
        temp = dict_to_write[i]
        filewrite.write(f"{i},{temp['game']},{temp['score']}\n")

write_to_file("heighest_score_internet_cafe/server_data.txt", data)