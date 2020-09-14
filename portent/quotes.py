"""Quote repository for portent."""
import random
from datetime import datetime

brass_eye_quotes = {

    # Brass Eye
    "UK used to mean United Kingdom, but ask anyone today and they'll "
    "tell you it stands for Unbelievable Krimewave.": "Chris Morris",

    "And last year, the mayor gave them a goldmine. It actually worked for "
    "a bit, this, until someone clogged it up with sick!": "Ted Maul",

    "What is cake? Well, it has an active ingredient which is a dangerous "
    "psychoactive compound known as "
    "\"dimesmeric andersonphospate\". It stimulates the part of the brain "
    "called \"Shatner's bassoon\", and that's the"
    " bit of the brain that deals with time perception. So a second feels like a month. "
    "Well, it almost sounds like "
    "fun, unless you're the Prague schoolboy who walked out into the street, straight "
    "in front of a tram. "
    "He thought he'd got a month to cross the street...": "Chris Morris",

    "What if a madman broke in here with a machine gun and shot you "
    "to pieces?": "Chris Morris",

    "This is the one thing we *didn't* want to happen.": "Chris Morris",

    "Luckily, the amount of heroin I use is harmless, I inject about once a "
    "month on a purely recreational basis.": "Chris Morris",

    "If you plot 'number of animals abused' against 'what makes people cruel' "
    "versus 'intelligence of either party', "
    "the pattern is so unreadable that you might as well just draw a chain of "
    "fox heads on sticks. And if you do that, "
    "an interesting thing happens: the word 'cruel' starts flashing. So - are "
    "we cruel to hunt foxes?": "Chris Morris",

    "For years, the system of tunnels and shafts has harboured a small "
    "population of wild horses without bothering the commuters.": "Ted Maul",

    "But now, say officials, the horses have become a menace.": "Ted Maul",

    "If time's a drug, then Big Ben is a huge needle injecting it "
    "into the sky.": "Chris Morris",

    "An overdose of heroin is fatal - in the short term. But there has been "
    "no research whatsoever into long term effects.": "Chris Morris",

    "Kids burst shops by filling them with rice, and pouring in water: "
    "then standing back and laughing, while the bricks are ripped apart by "
    "the swelling food.": "Ted Maul",

    "People say that alcohol's a drug. It's not a drug, "
    "it's a drink!": "Chris Morris",

    "Portillo’s teeth removed to boost pound.": "Chris Morris",

    "Nato annulled after delegate swallows treaty.": "Chris Morris",

    "Leicester man wins right to eat sister.": "Chris Morris",

    "Thank goodness, actually, they’re wearing gloves, because I’ve witnessed "
    "bare-knuckle boxing in a barn in Somerset about three years ago. And it "
    "was a sorry sight to see men goading them on in such a barbaric fashion. "
    "And I’m rather ashamed to say I was party to that "
    "goading.": "Alan Partridge",

    "I don’t know if you’ve seen Women In Love. There’s a marvellous scene "
    "by the fire. It kind of resembled that.": "Alan Partridge",

    "The atmosphere here hangs heavy, like a big smell. The smell of men "
    "together.": "Alan Partridge",

    "Due to a printing error, tomorrow’s Telegraph is full of "
    "water.": "Chris Morris",

    "On now to the money markets and a quick look at the International "
    "Finance Arse.": "Collaterlie Sisters",

    "Driving a car with bikes on the roof is not a sportsmanlike way to "
    "compete in the Tour de France.": "Alan Partridge",

    "They’ll quite simply say John Major punched the Queen, everything else "
    "will be a footnote": "Spartacus Mills",

    "You're wrong, and you're a grotesquely ugly freak.": "Chris Morris",

    "From the moon, Cowsick's a little dot. From the ground, it's a huge "
    "mess! Like Dante meets Bosch in a crack lounge!": "Ted Maul",

}


quotes_dict = {
    'satire': brass_eye_quotes,
}


def get_quote_and_attribution_tuple(genre=None):

    if not genre:
        genre = 'satire'

    random.seed(hash(str(datetime.utcnow())) * random.gauss(0, 1))
    d = quotes_dict[genre]
    quote = random.choice(list(d.keys()))
    attribution = d[quote]

    return quote, attribution
