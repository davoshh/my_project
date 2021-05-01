def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file has approximately {num_words} words.")


filenames = ['resources/chapter_10/alice.txt', 'resources/chapter_10/siddharth.txt',
             'resources/chapter_10/moby_dick.txt', 'resources/chapter_10/little_women.txt']
for filename in filenames:
    count_words(filename)
