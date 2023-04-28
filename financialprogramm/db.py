def insert_category(value):
    global counter
    categories.append((next(counter), value))
    print(f'Category {value} added')


def get_categories():
    return categories


def get_count():
    counter = 2
    while True:
        counter += 1
        yield counter


categories = [
    (1, 'food'),
    (2, 'taxi')
    ]
counter = get_count()
