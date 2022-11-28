import pygame

class Cell:
    def __init__( self, colour = (0,0,0), position = pygame.math.Vector2(0,0), velocity = (0,0), size = 2.5 ) -> None:
        
        
        
        self.colour = colour
        self.position = pygame.math.Vector2( position[0], position[1] )
        self.velocity = pygame.math.Vector2( velocity[0], velocity[1] )
        self.size = size

    def draw( self, screen ) -> None:
        pygame.draw.circle( screen, self.colour, (self.position.x+screen.get_size()[0]/2,self.position.y+screen.get_size()[1]/2), self.size )

    def update( self, deltaT ) -> None:
        self.position.x += self.velocity.x * deltaT
        self.position.y += self.velocity.y * deltaT
        if ( abs(self.position.x)+self.size > 250 ):
            self.velocity.x *= -1
        if ( abs(self.position.y)+self.size > 250 ):
            self.velocity.y *= -1
