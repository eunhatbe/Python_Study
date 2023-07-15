## 파이썬 데이터 모델
파이썬을 사용하다 보면 다른 객체지향 언어와 다른 차이점이 몇몇 있다. 예를들면 collection.len(); 라던지 프로퍼티를 지원하는 경우 collection.len을 사용하는 반면 파이썬은 len(collection)을 사용한다. 이러한 점을 "**파이써닉하다**"라고 하는데 이는 파이썬 데이터 모델이 제공하는 API를 이용해 개발자의 고유의 객체를 정의하면 대부분의 파이썬 사용구를 적용할 수 있다.

데이터 모델은 일종의 프레임워크로서, 파이썬을 설명하는 것이라고 생각할 수 있으며 시퀀스, 반복자, 함수, 클래스, 콘텍스트 관리자 등 언어 자체의 구성단위에 대한 인테페이스를 공식적으로 정의한다.

파이썬 인터프리터는 특별 메서드를 호출해서 기본적인 객체 연산을 수행하는데, 종종 특별한 구문에 의해 호출된다, 특별 메서드는 __getitem__() 처럼 언제나 앞뒤에 이중 언더바를 가지고 있다. 예를 들어 object[key] 형태의 구문은 __getitem__() 특별 메서드가 지원한다. collection[key]를 평가하기 위해 인터프리터는 collection.__getitem__(key)를 호출한다.
이러한 특별 메서드는 사용자가 구현한 객체가 다음과 같은 기본적인 언어 구조체를 구현하고 지원하고 함께 사용할 수 있게 해준다.

+ 반복
+ 컬렉션
+ 속성 접근
+ 연산자 오버로딩
+ 함수 및 메서드 호출
+ 객체 생성 및 제거
+ 문자열 표현 및 포맷
+ 블록 등 콘텍스트 관리

특별메서드는 마술메서드(magic method) 혹은 __method__() 의 더블 언더바를 줄인 던더메서드 라고도 한다.



## 카드 한 벌
다음 예제 코드는 특별 메서드 __getitem__()과 __len__()만으로 강력한 기능을 구현할 수 있다는 것을 보여준다.

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

```
먼저 collections.namedtuple()을 이용하여 개별 카드를 나타내는 클래스를 먼저 구현했다. 파이썬 2.6부터는 namedtuple을 이용하여 데이터베이스의 레코드처럼 메서드를 가지지 않는 일련의 속성으로 구성된 클래스를 만들 수 있다.

```bash
>>> beer_card = Card('7', 'diamonds')
>>> Card(rank='7', suit='diamonds')
```

하지만 이 코드의 핵심은 FrenchDeck 클래스이다. 먼저 일반적인 파이썬 컬렉션과 마찬가지로 len() 함수를 통해 자신이 갖고 있는 카드의 수를 반환한다.

