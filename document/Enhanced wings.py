# Simple butterfly information display

butterflies = {
    'Monarch': {
        'Scientific Name': 'Danaus plexippus',
        'Habitat': 'North America',
        'Fact': 'Monarch butterflies migrate over 3,000 miles each year.'
    },
    'Blue Morpho': {
        'Scientific Name': 'Morpho menelaus',
        'Habitat': 'Central and South American rainforests',
        'Fact': 'The Blue Morpho’s brilliant color comes from microscopic scales on its wings.'
    },
    'Swallowtail': {
        'Scientific Name': 'Papilio machaon',
        'Habitat': 'Worldwide',
        'Fact': 'Swallowtails have distinctive tails on their hindwings.'
    },
    'Glasswing': {
        'Scientific Name': 'Greta oto',
        'Habitat': 'Central America',
        'Fact': 'Glasswing butterflies have transparent wings that make them nearly invisible.'
    }
}

print("Enchanted Wings: Marvels of Butterfly Species\n")

for name in butterflies:
    print("Name:", name)
    print("Scientific Name:", butterflies[name]['Scientific Name'])
    print("Habitat:", butterflies[name]['Habitat'])
    print("Interesting Fact:", butterflies[name]['Fact'])
    print("-----------------------------")