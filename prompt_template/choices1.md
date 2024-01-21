---

Given the following narrative segment:

As you enter the bustling royal court of Prince Klum, you are greeted by the regal and wise ruler himself. The Prince approaches you with a kind smile, his piercing blue eyes shining with a sense of urgency.

"Greetings, brave adventurer," he says, extending a hand in friendship. "I have summoned you here today for a task of great importance. In the heart of the nearby Woods of Whispers, there dwells a powerful and mysterious Witch. This witch has created a potion of unparalleled magic, capable of granting wishes to those who possess it. However, she has gone missing, and her disappearance has left the kingdom in turmoil."

The Prince pauses, studying you intensely before continuing, "I charge you, brave adventurer, to find the Witch of the Woods and retrieve this potion. Bring it back to me, and I promise you will be rewarded beyond your wildest dreams. But be warned, the journey is treacherous and filled with danger. You must be cunning, quick-witted, and above all, brave." With that, the Prince nods and dismisses you, sending you off on your perilous quest.

---

Fate Master Task:

As the Fate Master, generate four actions the player should take to further the story and go deeper into the quest.  Your choices should lead the player in different direction and vary in consequence:

- One action should lead to a 'great' outcome, offering significant advantages or progress.
- Another action should lead to a 'poor' outcome, potentially causing setbacks or challenges.
- The remaining two actions should lead to 'good' outcomes, offering some benefits or positive developments.

Format the options in JSON for clarity and ease of integration into the game system.

Example of expected output:

{
    'choices': [
        {
            'description': '[Description of the great choice]',
            'outcome': 'great'
        },
        {
            'description': '[Description of the first good choice]',
            'outcome': 'good'
        },
        {
            'description': '[Description of the poor choice]',
            'outcome': 'poor'
        },
        {
            'description': '[Description of the second good choice]',
            'outcome': 'good'
        },
    ]
}
