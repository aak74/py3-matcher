class Matcher:
    PREFIXES = [
        'prod',
        'production',
        'test',
        'testing',
    ]
    SUFFIXES = [
        'az1',
        'az2',
    ]
    __new_projects = []
    __binds = None

    def match(self, projects: list, services: list):
        self.__new_projects = []
        self.__binds = dict()
        for project in projects:
            self.__binds[project] = []

        for service in services:
            if self.is_valid_with_prefix_and_suffix(service):
                continue

            if self.is_valid_direct(service):
                continue

            if self.is_valid_with_prefix(service):
                continue

            if self.is_valid_with_suffix(service):
                continue

            self.add_bind(service, service)

    def is_valid_direct(self, service: str):
        if service in self.__binds:
            self.add_bind(service, service)
            return True

        return False

    def is_valid_with_prefix(self, service: str):
        parts = service.split('_', 1)
        if len(parts) < 2:
            return False

        if parts[0] in self.PREFIXES:
            self.add_bind(parts[1], service)
            return True

        return False

    def is_valid_with_suffix(self, service: str):
        parts = service.rsplit('_', 1)
        if len(parts) < 2:
            return False

        if parts[1] in self.SUFFIXES:
            self.add_bind(parts[0], service)
            return True

        return False

    def is_valid_with_prefix_and_suffix(self, service: str):
        parts_prefix = service.split('_', 1)
        if len(parts_prefix) < 2:
            return False

        parts_suffix = parts_prefix[1].rsplit('_', 1)
        if len(parts_suffix) < 2:
            return False

        if parts_suffix[1] in self.SUFFIXES:
            self.add_bind(parts_suffix[0], service)
            return True

        return False

    def add_bind(self, project: str, service: str):
        if project not in self.__binds:
            self.__binds[project] = []
            self.__new_projects.append(project)

        self.__binds[project].append(service)

    def get_new_projects(self) -> list:
        return self.__new_projects

    def get_binds(self):
        return self.__binds
