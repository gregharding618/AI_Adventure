from bardapi import Bard, BardCookies

API_KEY = "AIzaSyAvWpd-YKEFoTq2l_eZj09KFbDcbf4I5Dg"

__Secure_1PSID = "agjBGmyGZ_LILNn4ATV3ktl-NNkFUfh7s75nGYak8sFHtLa-DfPG9ASL29_HBW7aCGQlHA."

cookie_dict = {
    "__Secure-1PSID": "agjBGmyGZ_LILNn4ATV3ktl-NNkFUfh7s75nGYak8sFHtLa-DfPG9ASL29_HBW7aCGQlHA.",
    "__Secure-1PSIDTS": "sidts-CjIB3e41hRCXHyZ-S0v5v5DjzGKE9nUAenz1-xMxV_2BVyDsdMpPSOciMNSb1sNFt1Gv0RAA",
    # Any cookie values you want to pass session object.
}

def main():
    while True:
        # bard = Bard(token=__Secure_1PSID)
        bard = BardCookies(cookie_dict=cookie_dict)
        user_input = input("\nEnter a message: ")
        response = bard.get_answer(f"You are an AI that generates C# code for Unity. You will only respond with code "
                                   f"that solves the prompt the user presents you. Do not add any dialogue, suggestions"
                                   f", explanations or comments that are not C# code. Respond with code and nothing but"
                                   f" code. User's prompt: {user_input}")['content']
        print(f"Response: {response}")


if __name__ == "__main__":
    main()
