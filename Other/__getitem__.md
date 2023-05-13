
### 첨자형 객체
파이썬에선 매직 메서드를 통해서 첨자형 객체를 만들수 있다.

보통 어떠한 배열의 마지막 인덱스에 있는 데이터를 가져올 때 아래와 같이 가져올 수 있다.
```python
array = [1,2,3,4]
last = array[array.__len__() - 1];
print(last)         # 4

last = array[len(array) - 1];
print(last)         # 4
```

하지만 이는 파이써닉 하지 않다. 파이썬에선 인덱스와 슬라이스 기능을 지원하기 때문에 위 코드는 다음과 같은 코드로 나타낼 수 있다.

```python
last = array[-1]
print(last)         # 4
```

파이써닉하게 인덱스를 다루는 기술은 아래와 같다.
```python
odds = array[::2]       # [1, 3]
evens = array[1::2]     # [2, 4]
sliced = array[2:4]     # [3, 4]
reverse = array[::-1]   # [4,3,2,1]
```

위와 같이 독특한 인덱싱과 슬라이싱 기능은 파이썬의 매직 매서드 덕분에 동작한다.

#### __getitem__
위 getitem 메서드를 구현한 객체를 첨자형 객체라고 한다.
```python
class Family:
    def __init__(self, member_size, *member) -> None:
        self._members : List[str] = list(member)
        self._memeber_count = member_size

    def add_memeber(self, member) -> None:
        self._members.append(member)
        self._member_count += 1
               
    def __getitem__(self, index) -> str:
        return self._members[index]
    
family = Family(3, "Mom", "Brother", "Sister")
family.add_member("Me")

print(family[3])
```

위 코드를 실행하면 "Me" 라는 값이 잘 출력된다. 하지만 만약 다음과 같은 코드를 실행한다면 에러가 발생한다.

```python
family[3] = "Jerry"
```

이는 __setitem__ 메서드를 정의해주지 않았기 때문에 동작하지 않는다. 다음 과같이 

```python
    def __setitem__(self, index: int, member: str) -> None:
        self._members[index] = member
```
를 정의해줘야한다.

```python
class Family:
    def __init__(self, member_size, *member) -> None:
        self._members : List[str] = list(member)
        self._member_count = member_size

    def add_member(self, member) -> None:
        self._members.append(member)
        self._member_count += 1
               
    def __getitem__(self, index) -> str:
        return self._members[index]
    
    def __setitem__(self, index: int, member: str) -> None:
        self._members[index] = member
    
family = Family(3, "Mom", "Brother", "Sister")
family.add_member("Me")

print(family[3])

family[3] = "Jerry"
print(family[3])
```
[결과]
```bash
Me
Jerry
```

또한 다음과 같이 for문에 들어가도 동작한다.
```python
for i in family:
    print(i)
```

[결과]
```bash
Mom
Brother
Sister
Jerry
```

위 코드는 __iter__ 를 사용하지 않았음에도 for에서 잘 동작하는데 이렇게 되는 이유는 파이썬이 객체를 통해 for loop를 작동하고자 할 떄 다음과 같은 순서로 체크하기 때문이다.

+ __iter__가 제공되는지 확인하고, 있으면 이를 통해 iter(obj)를 사용한다.
+ 만약 __iter__가 없다면 __getitem__ 이 있는지 확인하고 있으면 index 0 부터 시작해서 *IndexError* 가 발생할 때까지 __getitem__(index) 를 호출해서 for loop 를 작동신킨다.

이렇기 떄문에 __getitem__ 메서드가 정의 되어있으면 iterable type으로 취급되기 때문에 추가적인 코드 없이 위 동작이 가능한 것이다. 
