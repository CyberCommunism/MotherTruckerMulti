"""
Klasa której zadaaniem jest przechowywanie informacji o obecnie istniejących entity
wraz z ich komponentami, jest niczym baza danych a zastosowana struktura
wygląda następująco:
{
    "ComponentName": { (int)Entity.id : ComponentObject }
}
przykład:
{
    "HealthComponent": { 1 : (Object)<adres w pamięci> },
    "MoveComponent": { 1 : (Object)<adres w pamięci>, 2 : (Object)<adres w pamięci> }
}
"""


class EntityManager:

    def __init__(self):
        self._entities = []
        self._components = {}
        self._lowest_id = 0
        self.max_int = 10000
        self.entity_counter = 0
        self.entity_names = {}

    def remove_entity(self, entity_int):
        for comp_name in self._components.keys():
            if entity_int in self._components[comp_name].keys():
                self._components[comp_name].pop(entity_int)
        self.entity_counter -= 1
        self.entity_names.pop(entity_int)
        self._entities.remove(entity_int)

    def entity_number(self):
        return self.entity_counter

    def _new_id(self):
        if self._lowest_id < self.max_int:
            self._lowest_id += 1
            return self._lowest_id
        else:
            try:
                for i in range(1, self.max_int):
                    if not self._entities.__contains__(i):
                        return i
            except ValueError:
                print("Brakło inta czy coś, do zbadania")

    def create_entity(self, name):
        new_id = self._new_id()
        self._entities.append(new_id)
        self.entity_names[new_id] = name
        self.entity_counter += 1
        return new_id

    def add_component(self, component_to_add, entity_int):
        if component_to_add.name not in self._components.keys():
            self._components[component_to_add.name] = {}

        self._components[component_to_add.name][entity_int] = component_to_add

    def get_component_of_class(self, component_obj, entity):
        if component_obj.name in self._components and entity in self._components[component_obj.name]:
            return self._components[component_obj.name][entity]

    def get_all_entities_possessing_component_of_class(self, component_obj):
        if component_obj.name not in self._components:
            return []
        else:
            return list(self._components[component_obj.name].keys())
