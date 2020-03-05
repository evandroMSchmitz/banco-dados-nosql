import redis


class Redinsgo:

    def __init__(self):
        self.redis = redis.Redis()

    def setup(self):
        # fazer o set de numeros
        for i in range(1, 100):
            self.redis.sadd('setNumeros', i)
        
        # fazer a criação das cartelas, usuário e scores
        for user in range(1, 51):
            # criação dos usuário
            self.redis.hset(f'user:{user}', 'name', f'user{user}')
            self.redis.hset(f'user:{user}', 'bcartela', f'cartela:{user}')
            self.redis.hset(f'user:{user}', 'bscore', f'score{user}')

            # criação do score
            self.redis.zadd('score', {f'score{user}': 0})

            # criação da cartela
            for cartela in range (15):
                num = self.redis.srandmember('setNumeros')
                # validação pra não deixar a cartela ter numeros repetidos
                while self.redis.sismember(f'cartela:{user}', num):
                    num = self.redis.srandmember('setNumeros')
                
                self.redis.sadd(f'cartela:{user}', num)

            print(f'criou o user{user}')

if __name__ == '__main__':
    r = Redinsgo()
    r.setup()