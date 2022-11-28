import pygame

class EntityHandler:
    def __init__( self ) -> None:
        self.entityArray = []
        pass

    def draw( self, screen ) -> None:
        for entity in self.entityArray:
            entity.draw( screen )

    def update( self, deltaT ) -> None:
        for entity in self.entityArray:
            entity.update( deltaT )

    def addEntity( self, entity ):
        self.entityArray.append( entity )
        return entity
