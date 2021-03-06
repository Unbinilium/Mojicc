#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs
import hashlib

MOJIPLUSPLUS_VERSION = 'v0.0.7'
CPP_COMPILER = 'g++'

keywords_map = {
    u'↔': 'alignas',
    u'↩': 'alignof',
    u'☢': 'asm',
    u'🚗': 'auto',
    u'💡': 'bool',
    u'💔': 'break',
    u'💼': 'case',
    u'🚨': 'catch',
    u'🔥': 'char',
    u'🏫': 'class',
    u'💎': 'const',
    u'🗿': 'constexpr',
    u'💣': 'const_cast',
    u'➰': 'continue',
    u'🔎': 'decltype',
    u'😃': 'default',
    u'♻': 'delete',
    u'👇': 'do',
    u'✌': 'double',
    u'🎆': 'dynamic',
    u'❔': 'else',
    u'📇': 'enum',
    u'💋': 'explicit',
    u'🚀': 'export',
    u'🚪': 'extern',
    u'👎': 'false',
    u'⛵': 'float',
    u'🍀': 'for',
    u'🫂': 'friend',
    u'✈': 'goto',
    u'❓': 'if',
    u'⏳': 'inline',
    u'🔢': 'int',
    u'🐟': 'long',
    u'📻': 'mutable',
    u'📛': 'namespace',
    u'👶': 'new',
    u'🔇': 'noexcept',
    u'☠': 'nullptr',
    u'💿': 'operator',
    u'🏩': 'private',
    u'🏦': 'protected',
    u'⛪': 'public',
    u'☑': 'register',
    u'😈': 'reinterpret_cast',
    u'💩': 'return',
    u'🔬': 'short',
    u'➖': 'signed',
    u'📏': 'sizeof',
    u'⚡️': 'static',
    u'💂': 'assert',
    u'🎣': 'cast',
    u'🏠': 'struct',
    u'🤔': 'switch',
    u'💪': 'template',
    u'👉': 'this',
    u'🎁': 'thread_local',
    u'🔈': 'throw',
    u'👍': 'true',
    u'🚓': 'try',
    u'📤': 'typedef',
    u'🔍': 'typeid',
    u'⌨️': 'typename',
    u'💍': 'union',
    u'➕': 'unsigned',
    u'📥': 'using',
    u'👻': 'using',
    u'😱': 'void',
    u'⛽️': 'volatile',
    u'🔁': 'while'
}

def import_sources(path):
    try:
        with codecs.open(path, 'r', encoding='utf-8') as f:
            src = f.readlines()
            enc = str(src).encode(encoding='utf-8')
            hash = hashlib.sha1(enc).hexdigest()
            print("Moji++: Imported sources -> ['" + path + "']")
            return src, enc, hash
    except OSError:
        print("Moji++: Failed to import sources -> ['" + path + "']")
        exit(-1)
        
def phraser(src):
    phrased_src = []
    is_keep = False
    for line in src:
        segs = ''.join(line)
        phrased_line = {
            'to_trans': [],
            'transed': [],
            'to_keep': [],
            'index': []
        }
        final = {
            'transed': 0,
            'to_keep': 0,
            'line': []
        }
        for i, c in enumerate(segs):
            i_before = i - 1;
            if i_before < 0:
                i_before = 0
            if c == '\"':
                if segs[i_before] != '\\':
                    if not is_keep:
                        is_keep = True
                    else:
                        is_keep = False
            if not is_keep:
                if c == '\'':
                    if segs[i_before] != '\\':
                        if not is_keep:
                            is_keep = True
                        else:
                            is_keep = False
            if not is_keep:
                phrased_line['to_trans'].append(c)
                phrased_line['index'].append('transed')
            else:
                phrased_line['to_keep'].append(c)
                phrased_line['index'].append('to_keep')
        for trans in phrased_line['to_trans']:
            for c in trans:
                if c in keywords_map.keys():
                    phrased_line['transed'].append(keywords_map[c])
                else:
                    phrased_line['transed'].append(c)
        for type in phrased_line['index']:
            final['line'].append(phrased_line[type][final[type]])
            final[type] += 1
        line = ''.join(final['line'])
        phrased_src.append(line)
        print('\t' + line, end='')
    return phrased_src
        
        
def translate_sources(src, path, file_name):
    try:
        print("Moji++: Phrasing mpp sources to cpp -> ")
        translate_src = phraser(src)
    except OSError as err:
        print("Moji++: Failed to Phrasing mpp sources to cpp -> " + err)
    print("Moji++: Translate sources -> ['" + path + " >> " + file_name + "']")
    return translate_src
    
def export_sources(translate_src, file_name):
    try:
        with codecs.open(file_name, 'w', encoding='utf-8') as f:
            for line in translate_src:
                f.write(line)
            print("Moji++: Exported sources -> ['" + file_name + "']")
    except OSError as err:
        print("Moji++: Failed to export translated sources -> " + err)
        
def clean_up(file_names):
    for file_name in file_names:
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
            except OSError:
                print("Moji++: Failed to clean up exported sources -> '" + file_name + "'")
    print("Moji++: Clean up exported sources -> " + str(file_names))

def process_files(file_pathes):
    try:
        processed_files = []
        print("Moji++: Processing mpp files -> " + str(file_pathes))
        for path in file_pathes:
            src, enc, hash = import_sources(path)
            abs_path = os.path.join(os.path.dirname(path), hash + '.cpp')
            translate_src = translate_sources(src, path, abs_path)
            export_sources(translate_src, abs_path)
            processed_files.append(abs_path)
        print("Moji++: Processed mpp files -> " + str(file_pathes))
        return processed_files
    except OSError:
        print("Moji++: Failed to process mpp files -> " + str(file_pathes))

def compile_sources(handled_args, unhandled):
    try:
        print("Moji++: Compiling sources using " + CPP_COMPILER +" -> " + str(handled_args['-g']))
        processed_files = process_files(handled_args['-g'])
        pos = unhandled.index('-g') + 1
        unhandled[pos:pos] = processed_files
        command = CPP_COMPILER + ' ' + " ".join(unhandled)
        os.system(command)
        print("Moji++: Compilied sources using " + CPP_COMPILER +" -> " + str(handled_args['-g']))
        return processed_files
    except OSError as err:
        print("Moji++: Failed to compile sources -> " + str(handled_args['-g']) + '\n' + err)
        
def version():
    print("Moji++: An emoji AOT compilier for C++ alternative to g++, version -> " + MOJIPLUSPLUS_VERSION)
    command = CPP_COMPILER + ' -v'
    os.system(command)
        
def help():
    print("Moji++: An emoji AOT compilier for C++, the usage is alternative to g++ -> 'g++ --help'")
    command = CPP_COMPILER + ' --help'
    os.system(command)
        
def handle_arguments(args):
    app_next = False
    handled_args = {
        '-g': [],
        '-v': False,
        '--version': False,
        '--help': False
    }
    unhandled = []
    for arg in args:
        arg_s = str(arg)
        for key in handled_args.keys():
            if arg_s in key:
                if key != '-g':
                    handled_args[key] = True
                else:
                    app_next = True
        if app_next:
            if arg_s.split('.')[-1] == 'mpp':
                handled_args['-g'].append(arg_s)
            else:
                unhandled.append(arg_s)
        else:
            unhandled.append(arg_s)
    if handled_args['-v'] or handled_args['--version']:
        version()
        exit(0)
    elif handled_args['--help']:
        help()
        exit(0)
    else:
        return handled_args, unhandled
    
def main():
    args = sys.argv[1:]
    if len(args) < 2:
        args = "--help"
    handled_args, unhandled = handle_arguments(args)
    processed_files = compile_sources(handled_args, unhandled)
    clean_up(processed_files)
    return 0

if __name__ == '__main__':
    main()
    
