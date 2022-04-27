class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/popular?api_key=db79eaf5644a6dbd5134e36675c07332' 
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{550}?api_key={db79eaf5644a6dbd5134e36675c07332}' 



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True