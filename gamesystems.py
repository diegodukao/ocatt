from kivent_core.systems.gamesystem import GameSystem


class VelocitySystem2D(GameSystem):

    def update(self, dt):
        entities = self.gameworld.entities
        for component in self.components:
            if component is not None:
                entity_id = component.entity_id
                entity = entities[entity_id]
                position_comp = entity.position
                position_comp.x += component.vx * dt
                position_comp.y += component.vy * dt
