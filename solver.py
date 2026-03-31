from collections import deque


def get_neighbors(word, word_set):
    neighbors = []
    for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            new_word = word[:i] + c + word[i+1:]
            if new_word in word_set and new_word != word:
                neighbors.append(new_word)
    return neighbors


def word_ladder(start, end, word_set):
    if end not in word_set:
        return None

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        word = path[-1]

        if word == end:
            return path

        for neighbor in get_neighbors(word, word_set):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None
