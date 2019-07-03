#include <bits/stdc++.h>

using namespace std;

//Calcula o problema do caixeiro viajante utilizando Programação Dinâmica em O( n * 2^n )

void lerGraph(int n, vector<vector<int>> &cities){
    int num;
    
    //inicializar grafo
    cities.assign(n, vector<int>());
    
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            cin>>num;
            cities[i].push_back(num);
        }
    }
}

void stateGraph(vector<vector<int>> &state, vector<vector<int>> &cities){
    for(auto& neighbors : state)
        neighbors = vector<int>((1 << cities.size()) - 1, INT_MAX);
}

int tsp(const vector<vector<int>>& cities, int pos, int visited, vector<vector<int>>& state){
    if(visited == ((1 << cities.size()) - 1))
        return cities[pos][0]; // return para a cidade inicial

    if(state[pos][visited] != INT_MAX)
        return state[pos][visited];

    for(int i = 0; i < cities.size(); ++i){
        // não pode visitar si própria, a não ser que esteja terminando, e pular se a próxima ja foi visitada
        if(i == pos || (visited & (1 << i)))
            continue;

        int distance = cities[pos][i] + tsp(cities, i, visited | (1 << i), state);
        if(distance < state[pos][visited])
            state[pos][visited] = distance;
    }

    return state[pos][visited];
}

int main()
{
    int n;
    
    while( cin>>n ){
        vector<vector<int>> cities;
        
        lerGraph(n,cities);
    
        vector<vector<int>> state(cities.size());
        
        stateGraph(state, cities);

        cout << "Minimo: " << tsp(cities, 0, 1, state) << endl;
    }
    
    return 0;
}
