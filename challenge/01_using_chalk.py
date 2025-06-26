from chalk.client import ChalkClient

if __name__ == '__main__':
    c = ChalkClient()

    c.query(input={
        User.id: "1",
    }, output=[User.first_name])