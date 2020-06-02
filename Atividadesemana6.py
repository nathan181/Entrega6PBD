from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt

users = [
 {"id": 0, "name": "Hero"},
 {"id": 1, "name": "Dunn"},
 {"id": 2, "name": "Sue"},
 {"id": 3, "name": "Chi"},
 {"id": 4, "name": "Thor"},
 {"id": 5, "name": "Clive"},
 {"id": 6, "name": "Hicks"},
 {"id": 7, "name": "Devin"},
 {"id": 8, "name": "Kate"},
 {"id": 9, "name": "Klein"},
]


#print(users)

friendships = [
 (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

#lista de amigos vazia para cada usuário da rede
for user in users:
    user["friends"] = []

#percorre a lista de tuplas adicionando o usuário i à lista do usuário j e vice-versa

#for friendship in friendships:
#    users[friendship[0]]['friends'].append(users[friendship[1]])
#    users[friendship[1]]['friends'].append(users[friendship[0]])

#tuple unpacking
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

#print(users[0])

def number_of_friends(user):
    return len(user['friends'])

#print(number_of_friends(users[2]))

#[2, 3, 3, 2, 3] quantidade de amizades

#para cada usuario na colecao usuarios, eu quero uma expressão: number_of_friends
lista = [number_of_friends(user) for user in users]
#print(lista)

total_connections = sum(number_of_friends(user) for user in users)
#print(total_connections)

num_users = len(users)
avg_connections = total_connections / num_users

#print(avg_connections)

#[(0, 2), (1, 3), (2, 3)]


number_of_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

# print(number_of_friends_by_id)

#sorted - função de mais alta ordem, ou seja, pode receber função como parâmetro e devolver função

lista_ordenada = sorted(number_of_friends_by_id, key = lambda num_friends: num_friends[1], reverse=True )
#print(lista_ordenada)

def friends_of_friends_ids_bad(user):
    return [
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
    ]

#funcão decisora = função que toma uma decisão

def not_the_same (user, other_user):
    return user['id'] != other_user['id']


def not_friend(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user['friends'])

def friends_of_friends_ids (user):
    return set([
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friend(user, foaf)
    ])

#[True, True, False]
#[True, True, True]

#print(friends_of_friends_ids(users[0]))
# contagem = Counter([1, 2, 2, 3, 5, 5, 6, 7, 1])
# print(contagem)


def friends_of_friends_ids_frequency(user):
    return Counter([#contagem de quantos amigos em comum
        foaf['id']
        for friend in user['friends']
        for foaf in friend['friends']
        if not_the_same(user, foaf)
        and not_friend(user, foaf)
    ])

# print(friends_of_friends_ids_frequency(users[2]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

def data_scientists_who_like(target_interest):
    return [
        user_id for user_id, interest in interests if interest == target_interest
    ]

# print(data_scientists_who_like('MapReduce'))

# dicionario = {}
# print(dicionario['chave'])

# def teste():
#     return 'aeiou'

# dicionario = defaultdict(teste)
# print(dicionario['chave'])

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# print(user_ids_by_interest)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def users_with_common_interests_with (user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ])
# print(users_with_common_interests_with(users[0]))

def most_common_interests_with (user):
    return Counter (
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if (interested_user_id != user["id"])
    )
# print(most_common_interests_with(users[1]))

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)


average_salary_by_tenure = {
    tenure : sum (salaries)/len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
# print(average_salary_by_tenure)


def tenure_bucket (tenure):
    if tenure < 2:
        return "less than two"
    elif tenure <= 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# print(salary_by_tenure_bucket)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

# print(average_salary_by_bucket)

tenure_and_account_type = [
    (0.7, 'paid'),
    (1.9,'unpaid'),
    (2.5,'paid'),
    (4.2,'unpaid'),
    (6,'unpaid'),
    (6.5,'unpaid'),
    (7.5,'unpaid'),
    (8.1,'unpaid'),
    (8.7,'paid'),
    (10,'paid')
]


def predict_paid_or_unpaid (years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

words_and_counts = Counter(
    word
    for user, interest in interests
    for word in interest.lower().split()
)

for word, count in words_and_counts.items():
    if (count > 1):
        print(word, count)


# 1 Construa um gráfico de linha que mostra o número de amigos por usuário.

users_list = [user['name'] for user in users]
users_number_of_friends_list = [number_of_friends(user) for user in users]


plt.plot (users_list, users_number_of_friends_list, color='red', marker='o', linestyle='solid')
plt.title ("Número de amigos por usuário")
plt.ylabel ("Número de amigos")
plt.show()

# 2 Construa um gráfico de dispersão envolvendo salário e tempo de experiência.
salaries, tenures = [], []
for i, j in salaries_and_tenures:
    print(i, j)
    salaries.append(i)
    tenures.append(j)

print(salaries)
print(tenures)

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
plt.scatter (salaries, tenures)

for label, salaries_value, tenures_value in zip(labels, salaries, tenures):
    plt.annotate(
        label,
        xy = (salaries_value, tenures_value), # o ponto
        xytext = (5, -5), #o quão longe está o texto do ponto
        textcoords = 'offset points'
    )
plt.title ("Salário vs. Tempo de experiência")
plt.xlabel ("Salário")
plt.ylabel ("Tempo de experiência")
plt.show()


# 3 Construa um histograma envolvendo dados de pagantes e não pagantes.

list_tenures = []
for i, j in tenure_and_account_type:
    list_tenures.append(i)

print(list_tenures)

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 1 * 1 # calcula o decil

histogram = Counter(decile(grade) for grade in list_tenures)

print(histogram)
plt.bar(
    [  
        x for x in histogram.keys()
    ],
    histogram.values(),
    0.1
)

plt.axis ([-1, 11, 0, 10])# x: -5 a 105, y: 0 a 5
plt.xticks ([1 * i for i in range (11)])
plt.xlabel("Tempo de experiência")
plt.ylabel("Pagantes e não pagantes")
plt.title ("Pagantes e não pagantes por faixa de salário")
plt.show()


# 4 Construa um histograma de palavras em interesses. Por exemplo, a palavra learning pode
# aparecer em machine learning e em deep learning. Quebre cada interesse em palavras para fazer
# a contagem e montar o histograma.

words_and_counts = Counter(
    word
    for user, interest in interests
    for word in interest.lower().split()
)

print(words_and_counts)

# decile = lambda grade: grade // 1 * 1 # calcula o decil

histogram = words_and_counts

print(histogram)
plt.bar(
    [  
        x for x in histogram.keys()
    ],
    histogram.values(),
    0.5
)

plt.axis ([-1, 10, 0, 10])# x: -5 a 105, y: 0 a 5
plt.xticks ([1 * i for i in range (15)])
plt.xlabel("Menções de palavras por interesse")
plt.ylabel("Quantidades de menções do interesse")
plt.title ("Palavras por interesse")
plt.show()
