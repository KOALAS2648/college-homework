import os
def bubblesort(list):
    maxidx = len(list)-1
    sorted_list = list
    while True:
        #print(f"count:{count}")
        swapped = False
        for idx, number in enumerate(list):
            if idx != maxidx:
                compare = [list[idx], list[idx+1]]
            if compare[1] < compare[0]: # value at idx is smaller than the value at idx + 1
                sorted_list[idx]= compare[1]
                if idx != maxidx:
                    sorted_list[idx+1] = compare[0]
                    swapped = True
                else:
                    sorted_list[-1] = compare[0]
                    swapped = True
        if not swapped:
            break
    return sorted_list
def get_data(filename):
    file_data = list(open(filename, "r"))
    #print(file_data)
    for idx, line in enumerate(file_data):
        file_data[idx] = line[:-1].split(",")

    game_data = {}
    for values in file_data:
        game_data[values[0]] = {"game":values[1], "score":int(values[2])}
    return game_data

def get_scores_for_games(data):
    game_score_data = {"Minecraft":{"scores":[],"highscore":0, "players":[]},"Fortnite":{"scores":[], "highscore":0,"players":[]},"FIFA":{"scores":[], "highscore":0,"players":[]}}
    for value in data:
        j = data[value]["game"]
        game_score_data[j]["players"].append(value)
        game_score_data[j]["scores"].append(data[value]["score"])
        game_score_data[j]["highscore"] = max(game_score_data[j]["scores"])
    return game_score_data


def display_players_and_scores(data):
    for value in data:
        print(f"{value} got {data[value]['scores']} in {data[value]['game']}")

def display_scores_for_game(data, gamename):
    data[gamename]["scores"] = bubblesort(data[gamename]["scores"])
    for ans in data[gamename]["scores"]:
        print(f"{ans}")
    print(f"the average score for {gamename} is: {sum(data[gamename]["scores"])/len(data[gamename]["scores"])}")
    input()

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
        filewrite.write(f"{i},{temp['game']},{temp['score']}\n")
def fix_server(servername):
    data = get_data(servername)
    write_to_file(servername, data)
def main():
    fix_server("server_data.txt")
    while True:
        os.system("clear")
        dataM = get_data("server_data.txt")
        ask = input("1.do you want to add your score?\n2.Do you want to view the heighest score\n3.exit the progra?(1/2/3): ")
        if ask == "1":
            name = input("what is your name?: ")
            gamename = input("what game did you get your score in?: ")
            score = int(input("what was your score on the game?: "))
            dataM[name] = {"game":gamename, "score":score}
            write_to_file("server_data.txt", dataM)
        elif ask == "2":
            game = input("what game do you wan to view the scores of?: ")
            data = get_scores_for_games(dataM)
            display_scores_for_game(data, game)
        elif ask == "3":
            break

    print("thnaks for checking the internet")
if __name__ == "__main__":
    main()