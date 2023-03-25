import copy
from collections import Counter

selectors = generate_selectors()  # selectors is the set of all possible selectors aka SELECTORS

def CN2(TrainingSet): # CN2(E)
    ClassificationRuleList = [] # list of rules aka RULE_LIST
    while TrainingSet:
        # BestConditionExpression is best complex found aka BEST_CPX
        BestConditionExpression = Find_BestConditionExpression(TrainingSet) # Find_BestConditionExpression aka Find_Best_Complex
        if BestConditionExpression is not None: # if BEST_CPX is not None
            TrainingSubset = [example for example in TrainingSet if satisfies(BestConditionExpression, example)] # TrainingSubset is the subset of E covered by BEST_CPX aka E'
            TrainingSet = [example for example in TrainingSet if not satisfies(BestConditionExpression, example)] # TrainingSet is the subset of E not covered by BEST_CPX
            MostCommonClass = Counter(TrainingSubset).most_common(1)[0][0][-1] # MostCommonClass is the most common class in E' aka C
            rule = "if " + str(BestConditionExpression) + " then the class is " + str(MostCommonClass)
            ClassificationRuleList.append(rule)
        else:
            break
    return ClassificationRuleList # return RULE_LIST

def Find_BestConditionExpression(TrainingSet): # Find_BestConditionExpression(TrainingSet) aka Find_Best_Complex(E)
    ConditionalExpressionSet = [] # ConditionalExpressionSet is the set containing the empty complex aka STAR
    BestConditionExpression = None # BestConditionExpression is nil aka BEST_CPX
    while ConditionalExpressionSet: # while STAR is not empty
        TrialConditionalExpressionSet = generate_all_combinations(ConditionalExpressionSet) # TrialConditionalExpressionSet aka NEWSTAR
        TrialConditionalExpressionSet = [F for F in TrialConditionalExpressionSet if is_statistically_significant(F, TrainingSet)] # F aka Ci
        TrialConditionalExpressionSet = [F for F in TrialConditionalExpressionSet if is_better_than_best(F, BestConditionExpression, TrainingSet)]
        TrialConditionalExpressionSet.sort(key=complexity)
        while len(TrialConditionalExpressionSet) > MAX_EXPRESSIONS: # MAX_EXPRESSIONS is the maximum number of complex allowed aka user-defined maximum
            TrialConditionalExpressionSet = TrialConditionalExpressionSet[:-1] # remove the last element aka remove worst complex
        ConditionalExpressionSet = copy.deepcopy(TrialConditionalExpressionSet) # STAR = NEWSTAR
        BestConditionExpression = max(TrialConditionalExpressionSet, key=complexity) # BEST_CPX = max(NEWSTAR)
    return BestConditionExpression # return BEST_CPX

def satisfies(condition, example):
    for term in condition:
        if term not in example:
            return False
    return True

def is_statistically_significant(condition, training_set):
    # return True if condition is statistically significant in training_set
    pass

def is_better_than_best(condition, best_condition, training_set):
    # return True if condition is better than best_condition according to user-defined criteria
    pass

def complexity(condition):
    # return the complexity of the condition
    pass

def generate_all_combinations(condition_set): # generate_all_combinations of elements in condition_set aka SELECTORS
    # generate all possible combinations of conditions in condition_set
    pass

def generate_selectors(training_set):
    # generate all possible selectors
    pass

# Note that the functions is_statistically_significant(),
# is_better_than_best(), complexity(), and generate_all_combinations()
# are not defined in the provided pseudo code, so you'll
# need to implement them based on your specific use case.