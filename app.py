# Creating an app to calculate how many star points I need in brawl stars.

"""
Input: character, level, power points
output: character, power point needed, money needed
----------------------------------------------------

Take the first input and create a database.
| Character | Level | Power points |

Full list of all characters
Dictionary of {
    level 1 : {
        PPoints: 1410, money: 3090
        },
    level 2: {
        PPoints: 1390, money: 3070
        },
    ....
    }} 

For a user input, dict.get(input_value) return the value of PPoints money needed

Show these outputs in the UI
"""
import os
from functions import (
    get_level_info,
    create_df,
    check_brawler,
    add_brawler,
    update_brawler,
    save_df,
    order_database,
    input_brawler_check,
    input_level_check,
)

if __name__ == "__main__":
    make_change = True
    while make_change:

        # Fetching the level details
        main_level = get_level_info()

        # User input stage

        # Brawler name check
        brawler_check = True
        while brawler_check:
            input_brawler = input("[1/3] Brawler:").title()
            brawler_check = not input_brawler_check(input_brawler)
            if brawler_check:
                print(f'"{input_brawler}" is not a Brawler in the game')
            else:
                print(f'You are making changes to "{input_brawler}"')

        # Level check
        level_check = True
        while level_check:
            input_level = str(input("[2/3] Power level:"))
            level_check = not input_level_check(input_level)
            if level_check:
                print(
                    f'You have given "{input_level}" to {input_brawler}, which doesn\'t work in the game'
                )
            else:
                pass

        # Power point check
        pp_check = True
        while pp_check:
            input_pp = int(input("[3/3] Power points:"))
            req_pp = int(main_level.get(input_level).get("points")) - input_pp
            if req_pp < 0:
                print("Are you sure?")
            else:
                pp_check = False

        # Mapping the user input to return correct requirements
        req_pp = int(main_level.get(input_level).get("points")) - input_pp
        req_coin = main_level.get(input_level).get("coins")

        # Store the user input data into database
        db = create_df()

        if check_brawler(db, input_brawler):
            db = update_brawler(db, input_brawler, input_level, req_pp, req_coin)
        else:
            db = add_brawler(db, input_brawler, input_level, req_pp, req_coin)

        db = order_database(db)
        save_df(db)

        # Output stage to the user
        print("\n{}".format(db))

        print("\nMake change to another Brawler?")
        make_change_input = input("[y/n]:")
        if make_change_input == "n":
            make_change = False
        else:
            pass

