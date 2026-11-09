import pygame
import time

from mst_project import (
    linearSearch,
    binarySearchInSortedArray,
    BSTSearch,
    RBTSearch,
    insertBST,
    buildRB,
    genInput
)

pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('DSA Project')
font = pygame.font.SysFont('arial', 30)
clock = pygame.time.Clock()
FPS = 60

results = []
n = 1000
inputText = str(n)
typing = False
message = ''
algorithms = ['Linear Search', 'Binary Search', 'BST Search', 'RBT Search']
selected = [True, True, True, True]
missing = False


def button(text, x, y):
    pygame.draw.rect(window, (200, 200, 200), (x, y, 180, 40))
    window.blit(font.render(text, True, (0, 0, 0)), (x + 10, y + 5))


def runSearch():
    global results

    arr = genInput(n)
    sortedArr = sorted(arr)
    target = -1 if missing else arr[-1]

    bRoot = None
    for i in arr:
        bRoot = insertBST(bRoot, i)
    rRoot = buildRB(sortedArr)

    results = []

    if selected[0]:
        start = time.perf_counter()
        for i in range(1000):
            linearSearch(arr, target)
        results.append(('Linear Search', (time.perf_counter() - start) * 1000))

    if selected[1]:
        start = time.perf_counter()
        for i in range(1000):
            binarySearchInSortedArray(sortedArr, target)
        results.append(('Binary Search', (time.perf_counter() - start) * 1000))

    if selected[2]:
        start = time.perf_counter()
        for i in range(1000):
            BSTSearch(bRoot, target)
        results.append(('BST Search', (time.perf_counter() - start) * 1000))

    if selected[3]:
        start = time.perf_counter()
        for i in range(1000):
            RBTSearch(rRoot, target)
        results.append(('RBT Search', (time.perf_counter() - start) * 1000))


running = True
while running:
    window.fill((255, 255, 255))
    window.blit(font.render('DSA Search Algorithms', True, (0, 0, 0)), (30, 30))
    button('Run Search', 30, 90)
    window.blit(font.render('Input Size:', True, (0, 0, 0)), (30, 160))

    if typing:
        pygame.draw.rect(window, (100, 150, 255), (250, 160, 150, 40))
    else:
        pygame.draw.rect(window, (220, 220, 220), (250, 160, 150, 40))
    window.blit(font.render(inputText, True, (0, 0, 0)), (260, 165))

    for i in range(len(algorithms)):
        color = (160, 220, 170) if selected[i] else (220, 220, 220)
        pygame.draw.rect(window, color, (450, 90 + i * 55, 320, 40))
        text = ('[x] ' if selected[i] else '[ ] ') + algorithms[i]
        window.blit(font.render(text, True, (0, 0, 0)), (460, 95 + i * 55))

    pygame.draw.rect(window, (220, 220, 220), (450, 320, 320, 40))
    text = 'Target: Missing' if missing else 'Target: Present'
    window.blit(font.render(text, True, (0, 0, 0)), (460, 325))

    for i in range(len(results)):
        name, ms = results[i]
        text = name + ': ' + str(round(ms, 4)) + ' ms'
        window.blit(font.render(text, True, (0, 0, 0)), (30, 230 + i * 60))

    window.blit(font.render('Times are totals for 1000 searches.', True, (0, 0, 0)), (30, 470))
    window.blit(font.render(message, True, (200, 0, 0)), (30, 520))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 250 <= x <= 400 and 160 <= y <= 200:
                typing = True
            else:
                typing = False
            for i in range(len(algorithms)):
                if 450 <= x <= 770 and 90 + i * 55 <= y <= 130 + i * 55:
                    selected[i] = not selected[i]
                    results = []
            if 450 <= x <= 770 and 320 <= y <= 360:
                missing = not missing
                results = []
            if 30 <= x <= 210 and 90 <= y <= 130:
                if inputText.isdigit() and 10 <= int(inputText) <= 10000:
                    if any(selected):
                        n = int(inputText)
                        message = ''
                        runSearch()
                    else:
                        message = 'Select at least one algorithm'
                else:
                    message = 'Enter a number between 10 and 10000'
        if event.type == pygame.KEYDOWN and typing:
            if event.key == pygame.K_BACKSPACE:
                inputText = inputText[:-1]
            elif event.key == pygame.K_RETURN:
                typing = False
            elif event.unicode.isdigit() and len(inputText) < 5:
                inputText += event.unicode

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
