class Hello_world:
    text = 'Hello world!'
    def say(self):
        return self.text


if __name__ == "__main__":
    hello = Hello_world()
    print(hello.say())

