import pickle
import os
import pandas as pd


def input_brawler_check(input_brawler):
    brawler_list = [
        "Pam",
        "Penny",
        "Rico",
        "Jessie",
        "Nita",
        "Rosa",
        "Tick",
        "Mr.P",
        "Gale",
        "Colt",
        "Jacky",
        "Dynamike",
        "Tara",
        "Shelly",
        "Poco",
        "Bea",
        "El Primo",
        "Max",
        "Carl",
        "Darryl",
        "Piper",
        "Brock",
        "Frank",
        "Bo",
        "8-Bit",
        "Bibi",
        "Emz",
        "Bull",
        "Barley",
        "Mortis",
        "Sprout",
        "Gene",
        "Nani",
        "Spike",
        "Crow",
        "Leon",
        "Sandy",
        "Surge",
    ]
    return input_brawler in brawler_list


def input_level_check(input_level):
    return input_level in [str(level) for level in range(1, 10)]


def level_info_dict(level, points, coins):
    return dict([(level, dict([("points", points), ("coins", coins)]))])


def get_level_info():
    if not os.path.isfile("./level_info.pkl"):
        level_info = [
            ("1", 1410, 3090),
            ("2", 1390, 3070),
            ("3", 1360, 3035),
            ("4", 1310, 2960),
            ("5", 1230, 2820),
            ("6", 1100, 2530),
            ("7", 890, 2050),
            ("8", 550, 1250),
            ("9", 0, 0),
            ("10", 0, 0),
        ]

        main_level = dict()
        for level in level_info:
            level_dict = level_info_dict(level[0], level[1], level[2])
            main_level.update(level_dict)

        with open("./level_info.pkl", "wb") as file:
            pickle.dump(main_level, file)
        return main_level

    else:
        with open("./level_info.pkl", "rb") as file:
            main_level = pickle.load(file)
        return main_level


def create_df():
    if not os.path.isfile("./data/database.pkl"):
        df = pd.DataFrame(columns=["brawler", "power", "points", "coins"])
        with open("./data/database.pkl", "wb") as file:
            pickle.dump(df, file)
        return df
    else:
        with open("./data/database.pkl", "rb") as file:
            df = pickle.load(file)
        return df


def check_brawler(df, brawler):
    return brawler in df.brawler.to_list()


def add_brawler(df, brawler, power, points, coins):
    new_brawler = pd.DataFrame(
        [[brawler, power, points, coins]],
        columns=["brawler", "power", "points", "coins"],
    )
    df_added = df.append(new_brawler, ignore_index=True)
    return df_added


def update_brawler(df, brawler, power, points, coins):
    df.loc[(df.brawler == brawler), "power"] = power
    df.loc[(df.brawler == brawler), "points"] = points
    df.loc[(df.brawler == brawler), "coins"] = coins
    return df


def order_database(df):
    df_sorted = df.sort_values("points", ascending=True).reset_index(drop=True)
    return df_sorted


def save_df(df):
    with open("./data/database.pkl", "wb") as file:
        pickle.dump(df, file)
