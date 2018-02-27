class Friend(object):
    def __init__(self, friend_dict = None):
        """ initialize a graph object
            if no dictionary or None is given, an empty dictionary
            will be used.
        """
        if friend_dict is None:
            friend_dict = {}
        self.__friend_dict = friend_dict

    def people(self):
        # return the people of friend relations
        return list(self.__friend_dict.keys())

    def connections(self):
        # return a connection of two people
        return self.__make_connections()

    def add_people(self, people):
        # add a new people
        if people not in self.__friend_dict:
            self.__friend_dict[people] = []

    def add_connection(self, connection):
        # add a new connection between two people
        connection = set(connection)
        people1 = connection.pop()
        if connection:
            people2 = connection.pop()
        else:
            people2 = people1

        """every time two people have a connection, each of them
        becomes to the other's friend.
        """
        if people1 in self.__friend_dict:
            self.__friend_dict[people1].append(people2)
        else:
            self.__friend_dict[people1] = [people2]

        if people2 in self.__friend_dict:
            self.__friend_dict[people2].append(people1)
        else:
            self.__friend_dict[people2] = [people1]

    def __make_connections(self):
        """ A static method make connections of people"""
        connections = []
        for people in self.__friend_dict:
            for friends in self.__friend_dict[people]:
                connections.append({people, friends})
        return connections

    def __str__(self):
        allstr = "people: "
        for n in self.__friend_dict:
            allstr += str(n) + ""
        allstr += "\nconnections: "
        for connection in self.__make_connections():
            allstr += str(connection) + " "
        return allstr

    def can_be_connected(self, people1, people2, connected=[]):
        """ to check if people connect to specific one"""
        friend = self.__friend_dict
        connected = connected + [people1]
        if people1 == people2:
            return True
        if people1 not in friend:
            return False
        for people in friend[people1]:
            if people not in connected:
                ext_connected = self.can_be_connected(people, people2, connected)
                if ext_connected:
                    return True
        return False
