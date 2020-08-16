class unique_subsets:
    def sub_sets(self, set):
        return self.sub_sets_Recur([], sorted(set))

    def sub_sets_Recur(self, current, set):
        if set:
            return self.sub_sets_Recur(current, set[1:]) + self.sub_sets_Recur(current + [set[0]], set[1:])
        return [current]


print(unique_subsets().sub_sets([4, 5, 6]))
