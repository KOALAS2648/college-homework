def get_data(filename):
    file_data = list(open(filename, "r"))
    #print(file_data)
    for idx, line in enumerate(file_data):
        file_data[idx] = line[:-1].split(",")

    game_data = {}
    for values in file_data:
        game_data[values[0]] = {"game":values[1], "score":int(values[2])}
    return game_data

def get_heighest_score_for_games(data):
    game_score_data = {"Minecraft":{"scores":[], "players":[]},"Fortnite":{"scores":[], "players":[]},"FIFA":{"scores":[], "players":[]}}
    for value in data:
        j = data[value]["game"]
        game_score_data[j]["players"].append(value)
        game_score_data[j]["scores"].append(data[value]["score"])
        game_score_data[j]["scores"] = [max(game_score_data[j]["scores"])]
    return game_score_data


def display_players_and_scores(data):
    for value in data:
        print(f"{value} got {data[value]['score']} in {data[value]['game']}")

def display_scores_for_game(data, gamename):
    pass

def print_heightest_score(game, data):
    print(f"the players for this game : {game}")
    for i in data[game]['players']:
        print(f"{i}")
    print(f"this is the scorces for {game}")
    print(f"heighest score: {data[game]['scores'][0]}")

def write_to_file(filename, dict_to_write):
    filewrite = open(filename, "w")
    for i in dict_to_write:
        temp = dict_to_write[i]
        filewrite.write(f"{i},{temp['name']},{temp['score']}\n")

def main():
    while True:
        data = get_data("server_data.txt")
        display_players_and_scores(data)
        ask = input("1.do you want to add your score?\n2.Do you want to view the heighest score\n3.exit the progra?(1/2/3): ")
        if ask == "1":
            name = input("what is your name")
            gamename = input("what game did you get your score in?: ")
            score = int(input("what was your score on the game?: "))
            data[name] = {"game":gamename, "score":score}
        elif ask == "2":
            game = input("what game do you wan to view the scores of?: ")
