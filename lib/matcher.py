class Matcher:
    PREFIXES = [
        'prod',
        'production',
        'test',
        'testing',
    ]
    __new_projects = []
    __binds = None

    def match(self, projects: list, services: list):
        self.__new_projects = []
        self.__binds = dict()
        for project in projects:
            self.__binds[project] = []

        for service in services:
            if service in self.__binds:
                self.add_bind(service, service)
                continue

            parts = service.split('_', 1)
            if parts[0] in self.PREFIXES:
                self.add_bind(parts[1], service)
                continue

            self.add_bind(service, service)

    def add_bind(self, project: str, service: str):
        if service not in self.__binds:
            self.__binds[project] = []
            self.__new_projects.append(project)

        self.__binds[service].append(service)

    def get_new_projects(self) -> list:
        return self.__new_projects

    def get_binds(self):
        return self.__binds
