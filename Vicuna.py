import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = "r8_1Q04LqOgbrA1kT3X1nnlGXWyZ2wVKJf18PaW5"


def run_replicate():
    while True:
        try:
            user_input = input("\nEnter a message: ")
            output = replicate.run(
                "replicate/vicuna-13b:6282abe6a492de4145d7bb601023762212f9ddbbe78278bd6771c8b3b2f2a13b",
                input={
                    "prompt": user_input,
                    "randomness": 0
                }
            )

            for item in output:
                # https://replicate.com/replicate/vicuna-13b/versions/6282abe6a492de4145d7bb601023762212f9ddbbe78278bd6771c8b3b2f2a13b/api#output-schema
                print(item, end="")
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    run_replicate()

# export REPLICATE_API_TOKEN=r8_1Q04LqOgbrA1kT3X1nnlGXWyZ2wVKJf18PaW5
