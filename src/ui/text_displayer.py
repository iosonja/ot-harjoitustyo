import pygame


class TextDisplayer:
    """This class takes care of drawing text elements on the game view.

    Attributes:
        _window: The window to draw on.
    """

    def __init__(self, window):
        self._window = window

    def draw_scores(self, current_score):
        """Draw score tracker to the top left corner of the game view.
        """

        score_text = "Current score: {}".format(current_score)
        font = pygame.font.SysFont('ptmono', 25)
        self._window.blit(font.render(score_text, True, (0, 0, 0)), (10, 10))

    def draw_game_over(self, current_score):
        """Draw the end text and final score
        """

        text1 = "Well done!"
        text2 = "You finished with {} points.".format(current_score)
        font1 = pygame.font.SysFont('ptmono', 35)
        font2 = pygame.font.SysFont('ptmono', 30)
        self._window.blit(font1.render(text1, True, (0, 0, 0)), (500, 140))
        self._window.blit(font2.render(text2, True, (0, 0, 0)), (370, 180))

    def draw_nickname(self, nickname):
        text = "Enter nickname:"
        font = pygame.font.SysFont('ptmono', 20)
        self._window.blit(font.render(text, True, (0, 0, 0)), (510, 251))
        self._window.blit(font.render(nickname, True, (0, 0, 0)), (502, 281))

    def draw_answer_text(self):
        font = pygame.font.SysFont('ptmono', 20)
        answer_text = "Show the answer"
        self._window.blit(font.render(answer_text, True, (0, 0, 0)), (1005, 5))

    def reveal_answer(self, answer):
        font = pygame.font.SysFont('ptmono', 20)
        self._window.blit(font.render(answer, True, (0, 0, 0)), (1005, 5))
