## Spring

一个轻量级开发框架，旨在简化 J2EE EJB框架的复杂性

### Spring可以降低Java (J2EE) 开发的复杂性

基于POJO(Plain Old Java Object)/Java Bean的轻量级和最小侵入性编程

1.业务逻辑代码与框架代码解耦，可移植性强、易于单元测试

2.符合关注点分离的设计原则，提高了代码的组织性和可维护性

#### POJO类

普通的Java类，不继承子任何特殊的类，不实现任何特定的接口

不依赖于特定的框架，专注于数据存储和业务逻辑的实现，更接近业务逻辑的自然表达，可读性强，易于单元测试和迁移

可重用性强

与EJB完全相反

#### Lightweight Programming

轻量级容器：使用Servlet容器
简化配置：XML + 注解 + Java代码配置

#### 最小侵入性编程

POJO类中的业务逻辑代码无需继承Spring的类，实现Spring的接口，引入Spring框架的依赖

Bean定义、依赖关系、AOP配置等配置信息与业务代码分离

AOP无需修改原有代码，通过配置的方式为Bean组件添加日志记录、性能监控、事务管理等额外功能

`类似python的装饰器`

### Spring的设计目标

1.简化企业级应用开发，使开发者更专注于业务逻辑

2.提供一个适用于不同App的一致的编程模型

3.促进组件间解耦

4.方便应用其他技术，如JDBC、ORM、Web MVC等

### Spring的设计理念

#### Inversion Of Control

将对象的创建和依赖关系的管理从业务逻辑中分离，交由Spring容器管理

降低了组件间耦合度

#### Aspect Oriented Programming

将横切关注点（日志记录，事务管理等）从业务逻辑中分离，提高业务逻辑代码的模块化和可重用性

#### Interface Oriented Programming

一种编程范式，它强调使用接口（interface）而不是具体的实现类来定义模块之间的交互，要求分离接口与实现，降低耦合；由接口定义模块对外提供的服务和功能，由实现类负责实现

Spring AoP可以使用基于接口的代理模式实现切面织入

### Spring的核心

#### IoC 容器

管理Bean的生命周期和依赖关系

##### Bean的生命周期

1.Bean定义：从配置文件、注解或Java配置类中获取Bean的定义

2.实例化：Spring容器由Bean定义创建Bean实例

3.赋值(Construct)：容器将Bean属性值（如依赖）注入Bean实例中

4.初始化（可选）：调用被实现的InitializingBean接口的中的初始化方法

5.Bean被App使用

6.销毁：Spring容器关闭/Bean的作用域结束后被销毁，若Bean实现了DisposableBean接口，将在销毁前执行接口中destroy()方法

###### 相关接口与注解

InitializingBean: 提供afterPropertiesSet()

DisposableBean: 提供destroy()

@PostConstruct: 指定某方法用于Bean初始化

@PreDestroy: 指定某方法用于Bean销毁

#### AOP模块

定义切面{Pointcut Advice}

Pointcut定义切面目标对象，Advice定义切面操作

## Spring模块

Core Container + AOP + 设备支持 + Messaging + Web + 数据访问与集成

### Core Container

Core: 提供 IoC 和依赖注入功能

Beans: 提供BeanFactory，一个工厂模式的经典实现；Bean是Spring的管理对象

Context: 基于Core，提供一种框架式的对象访问方式

## Spring设计模式

1.工厂模式：将对象的创建逻辑封装在一个工厂类中，不在业务代码中实例化对象

2.单例模式: 一个类只有一个实例，必须自己创建自己的实例，为其他对象创建全局访问点

3.代理模式: 不直接操控目标对象，操控其代理（eg.快捷方式）；JDK的动态代理，CGLIB字节码生成技术

4.模板方法: 用于代码复用，如RestTemplate

5.观察者模式: ApplicationListener, 当某对象发生改变时通知所有依赖它的对象

## Spring中的事件

1.ContextRefreshedEvent: ConfigurableApplicationContext接口中定义

2.ContextStartedEvent: ConfigurableApplicationContext接口中定义

3.ContextStoppedEvent: ConfigurableApplicationContext接口中定义

4.ContextClosedEvent: ApplicationContext被关闭时触发；容器关闭时，其中所有单例Bean都被销毁

5.RequestHandledEvent: Web应用中一个http请求结束时触发

事件可通知实现了ApplicationListener接口的Bean



