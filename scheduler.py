import controller

def main():
    args = vars(controller.parse_args())
    func = args.pop('func', None)
    func(*args.values())


if __name__ == "__main__":
    main()
