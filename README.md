## Mojicc

An emoji AOT compilier set for C/C++, which helps you to code C/C++ with emojis, inspired by paper ["Enhancing the C++ Basic Character"](https://isocpp.org/files/papers/PO3OOrO.pdf), not the implementation but just play for fun.

Simply write source files extension with `.mpp` that can be compiled with **moji++ compiler**:

```cpp
#include <iostream>
π₯ π std;
π’ main(π’ argc, π₯ ** argv) { 
   cout << "Hello Emoji π!";
   π© 0;
}
```

Then compile the source code and execute the binary. Itβs okey to compile `.mpp` with `.cpp` source files, the compiler will handle sources files and command arguments automatically.

```shell
moji++ -g main.mpp -o main
./main
> Hello Emoji π!
```

## Get started

Install mojicc dependencies:

 - `python3` for running mojicc AOT compiler
 - `gcc` or alternative compiler for compiler translated cpp source files

Download mojicc AOT compiler source code and set up environment variables:

```shell
git clone https://github.com/Unbinilium/Mojicc.git mojicc
alias 'moji++'="python3 $(pwd)/mojicc/src/moji++/moji++.py"
```

Check your mojicc installation by `moji++ -v`. 

The moji++ AOT compiler actually call the cpp compiler after mpp source files translated to cpp source files, so that you could use the arguments as same as the cpp compilers, the only difference is that mojicc AOT compiler filter the source file names with `.mpp` extension and do the translation.

It means this is not something like mojilang, that only C++. You can write code by replacing keywords in C++ to emoji follow the unicode conversions table below, furthermore, you should know that:

- moji++ AOT compiler only replaces the keywords, not the emoji in the "" or '' evenif it is in the unicode conversions table
- moji++ AOT compiler will do changes to your comments if it contains the same emoji in the unicode conversions table

## Unicode conversions table

|  Keyword   | Emoji |   Keyword    | Emoji |  Keyword  | Emoji |     Keyword      | Emoji | Keyword  | Emoji |
| :--------: | :---: | :----------: | :---: | :-------: | :---: | :--------------: | :---: | :------: | :---: |
|  alignas   |   β   |   continue   |   β°   |  friend   |   π«   |     register     |   β   |   true   |   π   |
|  alignof   |   β©   |   decltype   |   π   |   goto    |   β   | reinterpret_cast |   π   |   try    |   π   |
|    asm     |   β’   |   default    |   π   |    if     |   β   |      return      |   π©   | typedef  |   π€   |
|    auto    |   π   |    delete    |   β»   |  inline   |   β³   |      short       |   π¬   |  typeid  |   π   |
|    bool    |   π‘   |      do      |   π   |    int    |   π’   |      signed      |   β   | typename |   β¨   |
|   break    |   π   |    double    |   β   |   long    |   π   |      sizeof      |   π   |  union   |   π   |
|    case    |   πΌ   | dynamic_cast |  π_π£  |  mutable  |   π»   |      static      |   β‘   | unsigned |   β   |
|   catch    |   π¨   |     else     |   β   | namespace |   π   |  static_assert   |  β‘_π  |  using   |   π₯   |
|    char    |   π₯   |     enum     |   π   |    new    |   πΆ   |   static_cast    |  β‘_π£  | virtual  |   π»   |
|  char16_t  | π₯16_t |   explicit   |   π   | noexcept  |   π   |      struct      |   π    |   void   |   π±   |
|  char32_t  | π₯32_t |    export    |   π   |  nullptr  |   β    |      switch      |   π€   | volatile |   β½   |
|   class    |   π«   |    extern    |   πͺ   | operator  |   πΏ   |     template     |   πͺ   | wchar_t  | wπ₯_t  |
|   const    |   π   |    false     |   π   |  private  |   π©   |       this       |   π   |  while   |   π   |
| constexpr  |   πΏ   |    float     |   β΅   | protected |   π¦   |   thread_local   |   π   |          |       |
| const_cast |   π£   |     for      |   π   |  public   |   βͺ   |      throw       |   π   |          |       |

## License

[MIT License](https://github.com/Unbinilium/Mojicc/blob/main/LICENSE) Copyright (c) 2021 Unbinilium.
