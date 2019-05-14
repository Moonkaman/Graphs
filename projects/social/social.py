import random
import sys
sys.path.append('../graph')
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(numUsers ^ 2)
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(numUsers ^ 2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(1)
        random.shuffle(possibleFriendships)

        # Time Complexity: O(avgFriendships * numUsers // 2)
        # Space Complexity: O(avgFriendships * numUsers // 2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

            def bfs(self, starting_vertex, destination_vertex):
        """
        visited = {}

        qu = Queue()
        qu.enqueue(userID)
        while qu.size() > 0:
            user = qu.dequeue()
            if user not in visited:
                print(user)
                visited[user] = None
                for n in self.friendships[user]:
                    if n not in visited:
                        qu.enqueue(n)
        print('------------------')
        print(visited)
        print('------------------')

        # Create an empty Queue
        for f in visited:
            print(f)
            q = Queue()
            # Create an empty Visited set
            been = set()
            # Add A PATH TO the starting vertex to the queue
            q.enqueue([userID])
            # While the queue is not empty...
            while q.size() > 0:
                # Dequeue the first PATH
                path = q.dequeue()
                # Grab the last vertex of the path
                v = path[-1]
                # Check if it's our destination
                if v == f:
                    visited[f] = path
                    break
                # If it has not been visited...
                if v not in been:
                    # Mark it as visited (add it to the visited set)
                    been.add(v)
                    # Then enqueue PATHS TO each of its neighbors in the queue
                    for neighbor in self.friendships[v]:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        q.enqueue(path_copy)
            # Note that this is a dictionary, not a set
            # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
