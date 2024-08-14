import argparse

def main(param1, param2):
    print('HELLOOOO')
    print(f"Param1: {param1}")
    print(f"Param2: {param2}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Accepts two parameters")
    parser.add_argument("param1", type=str, help="First parameter")
    parser.add_argument("param2", type=int, help="Second parameter")
    args = parser.parse_args()
    main(args.param1, args.param2)
