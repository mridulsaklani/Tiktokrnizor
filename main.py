import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab size: ", encoder.n_vocab)  # it is showing vocab size of model supperded as well..


text = "Mridul was good boy... % #^* "

generate_token = encoder.encode(text)

print("generated token: ",generate_token)

my_token= [24891, 315, 361, 673, 1899, 8473, 1008, 1851, 1069, 61, 9, 220]

parse_token = encoder.decode(my_token)

print(parse_token)